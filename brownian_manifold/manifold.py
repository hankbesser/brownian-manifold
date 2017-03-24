#test
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
# Ignore the unused warning: Axes3D import
# enables projection='3d' to be used without error
from mpl_toolkits.mplot3d import Axes3D

from utils import vector_cross, arctan2, surface_sphere, surface_cylinder

class Manifold(object):
    """
    Class that implements a few conveniences for simulating and
    visualizing the trajectory of Brownian motion on a manifold embedded
    in three-dimensional Euclidian space.

    For the purpose of this class, We allow for the simulation of
    Brownian Motion on two types of manifolds;

    1. A 2-sphere

    2. A finite cylinder

    Note
    ----------
    For a more involved simulation incorporating the Manifold objects:
    head on over to the Diffusion class
    in brownian-manifold.diffusion

    Parameters
    ----------
    manifold: can be either 'sphere' or 'cylinder'

        manifold = 'sphere'  ;

        Generalized approach using the "Tangent Space" of 2-sphere
        to run Brownian Motion simulation

        manifold = 'cylinder'  ;

        Generalized approach using the fact the finite cylinder
        is a "manifold with boundary" to run Brownian Motion simulation

    final_time: float, total time of simulation
    (assumption: initial time of simulation is always 0)

    n_steps: int, number of steps (i.e the intervals to split [0,final_time])

    radius_sphere: float, radius of sphere

    radius_cylinder: float, radius of cylinder

    height_cylinder: float, height of cylinder

    Internal variables
    ------------------
    store_matrices_: float,  3 x 3 x n_steps, rotation matrix

    Callable Methods
    -------
    simulate_brownian_sphere

    plot_brownian_sphere

    simulate_brownian_cylinder

    plot_brownian_cylinder

    get_sphere

    plot_sphere

    get_cylinder

    plot_cylinder

    Class methods
    -------------
    _rot_matrix

    _smooth_and_rotate
    """

    def __init__(self,
                 manifold='sphere',
                 radius_sphere = 1,
                 radius_cylinder = 1,
                 height_cylinder = 10,
                 final_time=1,
                 n_steps=1000):
        """
        Initialize the object
        """
        self.manifold = manifold
        self.final_time = float(final_time)
        self.n_steps = int(n_steps)
        self.step_size = (self.final_time/self.n_steps)
        # Assign random rotation matrix parameter
        # -------------------------------
        self.store_matrices_ = np.zeros((3,3,n_steps))
        # Assign manifold parameters
        # -------------------------------
        # Default 2-sphere: the unit 2-sphere, the surface of a unit ball.
        # i.e radius_sphere = 1
        self.radius_sphere = radius_sphere
        ###Defaults finite cylinder: radius = 1 and height = 10
        self.radius_cylinder = radius_cylinder
        self.height_cylinder = height_cylinder
    # for debugging purposes- does not affect functionality
    #-------------------------------------------------------------
        if self.manifold not in ('sphere', 'cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(self.manifold))


    def __repr__(self):
        """An internal representation"""
        return "{0}(manifold='{1}')".format(
                self.__class__.__name__, self.manifold)


    def __str__(self):
        """The string to be printed"""
        return "The manifold is a {0}!".format(self.manifold)


    # -----------------------------------------------------------------------
    def simulate_brownian_sphere(self, manifold=None, plot=False):
        """

        1. Implementation of '_smooth_and_rotate' class method:

        Walks generated in tangent plane, which touches
        the 2-sphere at the "north" pole point. The walks draw
        Gaussian Random numbers in R^2 with a scale based on the 'final_step'
        and 'n_steps' parameters input to the Manifold class.
        Each walk generated at north pole has a unique/random smoothed
        position on the 2-sphere and a unique/random rotation matrix
        to rotate back to north pole. These smoothed positions and
        rotation matrices are computed and pre-allocated in memory
        for future use.

        2. Implementation of Rodrigues' rotation formula
        using the '_rot_matrix' class method:

        The first walk is smoothed onto the sphere (representing
        a particle's first step on the 2-sphere). The pre-allocated
        rotation-matrix (computed with '_smooth_and_rotate' class method)
        rotates the particle back to the north pole.
        This same process ensues for the particle's new position smoothed onto
        the sphere, but the the newly smoothed step and the first step
        are rotated alike (with the newly generated step rotated back
        to the north pole). A total of n_steps (user-specified)
        are rotated back to the north pole with the total walks to rotate
        growing linearly as the particle's  steps progresses.
        The algorithm's' success (in terms of implementation) can be noted by
        the position of the last step when inspecting the returned data,
        'browniansphere'. The final position should be [0,0,radius_sphere]
        (with minimal rounding error), as this is the position of the north pole
        for 2-sphere embedded in three-dimensional Euclidian space
        """

        if manifold is None:
            manifold = self.manifold
        # for debugging purposes- does not affect functionality
        #-------------------------------------------------------------
        if manifold is 'cylinder':

            raise NameError('the cylinder manifold is not used\n\
            for the simulate_brownian_sphere method!\n\
            Use simulate_brownian_cylinder method instead!')

        if manifold not in ('sphere','cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(manifold))
        #------------------------------------------------------------
        smoothpositions, rotationmatricies= self._smooth_and_rotate()
        # arbitrary vector just used for initial update column vector for the
        # matrix rotation...but the vector doesn't factor into the data.
        updator = np.array([[0],[0],[0]])

        for i in range (self.n_steps):
            position_vector_temp=np.reshape(smoothpositions[:,i],(3,1))
            position_vector_temp2 = np.append(updator,
                                              position_vector_temp,axis=-1)
            final_data_frame = np.dot(rotationmatricies[:,:,i],
                                      position_vector_temp2)
            updator = final_data_frame
        browniansphere = np.transpose(final_data_frame[:,1:])
        # Show the Brownian Motion simulation
        # on 2-sphere (with defaults). will be a snapshot of all n_steps
        # use plot_simulation_sphere method to mess around with plot
        if plot is True:
            self.plot_brownian_sphere(browniansphere)

        return browniansphere


    # -----------------------------------------------------------------------
    def plot_brownian_sphere(self, sphere_bm,
                                     manifold=None,
                                     surface_color= 'red',
                                     colorbar='viridis',
                                     marker='.',
                                     markersize=4,
                                     steptoplot=None,
                                     has_title=True,
                                     show_axes=False):
        if manifold is None:
            manifold = self.manifold
        # for debugging purposes- does not affect functionality
        #-------------------------------------------------------------
        if manifold is 'cylinder':
            raise NameError('the cylinder manifold is not used\n\
            for the plot_brownian_sphere method!\n\
            Use plot_brownian_cylinder method instead!')

        if manifold not in ('sphere','cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(manifold))
        #------------------------------------------------------------
        if steptoplot is None:
            steptoplot = [self.n_steps]
        elif type(steptoplot) is int:
            steptoplot=[steptoplot]
        elif len(steptoplot)>4:
            raise ValueError('can only plot up to 4 snapshots!')
        else:
            steptoplot=steptoplot

        if any(x > self.n_steps for x in steptoplot):
            raise ValueError('you chose step(s) > {0} (the total steps)'\
                             .format(self.n_steps))

        if any(x <=0 for x in steptoplot):
            raise ValueError('you chose one or more invalid\n\
            step(s) to plot')

        fig = plt.figure(figsize=(10,10))

        if has_title:
            fig.suptitle('Brownian Motion Simulation\n on 2-Sphere Manifold:\n Total Steps= {0}\n Step Size = {1:.5f}'\
                         .format(self.n_steps,self.step_size),
                         fontsize=9, weight='bold')

        for i in range(len(steptoplot)):
            if len(steptoplot)==1:
                ax=fig.add_subplot(1,1,1,projection='3d')
            elif len(steptoplot)==2:
                ax=fig.add_subplot(2,1,i+1,projection='3d')
            else:
                ax=fig.add_subplot(2,2,i+1,projection='3d')

            timebar = np.arange(1,steptoplot[i]+1,1)
            brown = ax.scatter(sphere_bm[0:steptoplot[i],0],
                               sphere_bm[0:steptoplot[i],1],
                               sphere_bm[0:steptoplot[i],2],
                               c=timebar, cmap=colorbar,
                               marker=marker,
                               s=markersize,
                               facecolor='0.5', lw = 0,
                               label ='Snapshot at step {0}'.format(steptoplot[i]))

            surface = self.get_sphere()
            ax.plot_surface(surface[0],
                            surface[1],
                            surface[2],
                            rstride=1, cstride=1, linewidth=0,
                            color=surface_color, alpha=0.06)
            ax.view_init(elev=2)
            ax.set_xticks([-self.radius_sphere,0,self.radius_sphere])
            ax.set_yticks([-self.radius_sphere,0,self.radius_sphere])
            ax.set_zticks([-self.radius_sphere,0,self.radius_sphere])
            ax.set_xlabel('X',linespacing=2.2,fontsize=8)
            ax.set_ylabel('Y',linespacing=2.2,fontsize=8)
            ax.set_zlabel('Z',linespacing=2.2,fontsize=8)
            ax.set_xlim([-self.radius_sphere, self.radius_sphere])
            ax.set_ylim([-self.radius_sphere, self.radius_sphere])
            ax.set_zlim([-self.radius_sphere, self.radius_sphere])
            ax.set_aspect("equal")
            ax.tick_params(axis='both', which='both', pad=0.01)
            ax.legend(fontsize=9,loc='best')

            if show_axes is False:
                ax.set_axis_off()

            cbar = fig.colorbar(brown, ax=ax,
                                fraction=.12,pad=.053,
                                shrink=0.5)
            cbar.set_label('step number',size=8)
            cbar.ax.tick_params(labelsize=8)
            plt.tight_layout()
            plt.tick_params(labelsize=7)
        plt.show()
        #Save the full figure..
        #fig.savefig('name_of_file')


    # -----------------------------------------------------------------------
    def _smooth_and_rotate(self):

        """
        Approximates Brownian motion on a 2-sphere by finding a
        Brownian step in tangent space associated with the north pole
        point of a 2-sphere embedded in three-dimensional Euclidian
        space. The step found in Tangent Space is smoothed onto sphere and
        a rotation matrix is computed (using the '_rot_matrix' class method)
        and stored in memory for use in simulations.
        """
        rotation_matrices = self.store_matrices_
        # Approximate Brownian Motion on sphere
        # Finds a Brownian step on tangent plane
        x_coord = stats.norm.rvs(scale=np.sqrt(self.step_size),
                                 size = self.n_steps)
        y_coord = stats.norm.rvs(scale=np.sqrt(self.step_size),
                                 size = self.n_steps)
        step_size = np.sqrt(x_coord**2 +y_coord**2)
        # Smooths the step onto the sphere
        theta = arctan2(y_coord,x_coord)
        phi = step_size/self.radius_sphere
        smoothed_positions=np.array([
                                self.radius_sphere*np.cos(theta)*np.sin(phi),
                                self.radius_sphere*np.sin(theta)*np.sin(phi),
                                self.radius_sphere*np.cos(phi)])
        for i in range(self.n_steps):
            # rotates the sphere so that the
            # last step is positioned at the North pole
            # using the _rot_matrix (class method)
            rotation_matrices[:,:,i] = self._rot_matrix(
                                                    smoothed_positions[:,i],
                                                    phi[i])
        return smoothed_positions, rotation_matrices


    # -----------------------------------------------------------------------
    def _rot_matrix(self,v, phi):
        """
        Rotation matrix based on the Rodrigues rotation formula.
        For more information about the expressions,
        see the Rodrigues rotation formula wikipedia page at:
        https://en.wikipedia.org/wiki/Rodrigues'_rotation_formula

        Parameters
        ----------
        v: array

        phi: float

        Returns
        -------
        R: ndarray, the resulting rotation matrix
                that rotates the vector (parameter v) by an angle
                (parameter phi) so that v is rotated in to
                [0,0,radius_sphere] in three-dimensional
                Euclidian Space--i.e. the north pole of the sphere.
        """

        cross = vector_cross(v=v,w=np.array([0,0,1]))
        # normalizes the axis vector
        cross_norm = cross/(np.sqrt(np.dot(cross,cross)))
        cp_matrix = np.array([[0,-cross_norm[2],cross_norm[1]],\
                          [cross_norm[2],0,-cross_norm[0]],\
                          [-cross_norm[1],cross_norm[0],0]])
        # identity matrix
        I= np.eye(3)
        R = I + np.sin(phi)*cp_matrix + (1 - np.cos(phi))*\
                                    (np.dot(cp_matrix,cp_matrix))
        return R


    # -----------------------------------------------------------------------
    def get_sphere(self, manifold=None, plot=False):

        """
        Compute a blank 2-sphere and plot the surface (if specified)

        Parameters
        ----------
        radius_sphere: float, radius of sphere

        manifold: str, 'sphere'

        plot: bool, if True then plot

        Returns
        -------
        spheresurface : ndarray

        Note
        -------------------------------------------------
        the spheresurface "data" is only used for plotting
        the blank surface of 2-sphere.
        """

        if manifold is None:
            manifold = self.manifold
        # for debugging purposes- does not affect functionality
        #-------------------------------------------------------------
        if manifold is 'cylinder':
            raise NameError('the cylinder manifold is not used\n\
            for the get_sphere method!\n\
            Use get_cylinder method instead!')

        if manifold not in ('sphere','cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(manifold))
        #------------------------------------------------------------
        spheresurface = surface_sphere(self.radius_sphere)
        # Show the sphere (with defaults) or not
        if plot is True:
            self.plot_sphere(spheresurface)

        return spheresurface


    # -----------------------------------------------------------------------
    def plot_sphere(self,sphere_surface,
                    manifold=None,
                    color='cyan', alpha=0.2,
                    antialiased=False, has_title=True,show_axes=False):

        if manifold is None:
            manifold = self.manifold
        # for debugging purposes- does not affect functionality
        #-------------------------------------------------------------
        if manifold is 'cylinder':
            raise NameError('the cylinder manifold is not used\n\
            for the plot_sphere method!\n\
            Use plot_cylinder method instead!')

        if manifold not in ('sphere','cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(manifold))
        #------------------------------------------------------------
        plt.figure()
        ax = plt.gca(projection='3d')
        #no need to change rstride,cstride,or linewidth
        #hence they are not given in the method header.
        ax.plot_surface(sphere_surface[0], sphere_surface[1], sphere_surface[2],
                        rstride=1, cstride=1, linewidth=0,
                        antialiased=antialiased, color=color, alpha=alpha)
        if has_title:
            plt.title('Surface Plot: 2-sphere')

        ax.set_aspect('equal')
        ax.view_init(elev=10)
        ax.set_xticks([-self.radius_sphere,0,self.radius_sphere])
        ax.set_yticks([-self.radius_sphere,0,self.radius_sphere])
        ax.set_zticks([-self.radius_sphere,0,self.radius_sphere])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        if show_axes is False:
            ax.set_axis_off()
        plt.show()


    # -----------------------------------------------------------------------
    def get_cylinder(self, manifold=None, plot=False):

        """
        Compute a blank finite cylinder and plot the surface (if specified)

        Parameters
        ----------
        radius_cylinder: float, radius of cylinder

        height_cylinder: float, radius of cylinder

        manifold: str, 'cylinder'

        plot: bool, if True then plot

        Returns
        -------
        sphere_surface : ndarray

        Note
        -------------------------------------------------
        the sphere_surface "data" is only used for plotting
        the blank surface of 2-sphere.

        """
        if manifold is None:
            manifold = self.manifold

        # for debugging purposes- does not affect functionality
        #-------------------------------------------------------------
        if manifold is 'sphere':
            raise NameError('the sphere manifold is not used\n\
            for the get_cylinder method!\n\
            Use get_sphere method instead!')

        if manifold not in ('sphere','cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(manifold))
        #------------------------------------------------------------
        cylindersurface = surface_cylinder(self.radius_cylinder,
                                           self.height_cylinder)
        # Show the cylinder (with defaults) or not
        if plot is True:
            self.plot_cylinder(cylindersurface)

        return cylindersurface


    # -----------------------------------------------------------------------
    def plot_cylinder(self, cylinder_surface,
                      manifold=None,
                      color='cyan', alpha=0.15,
                      antialiased=False, has_title=True,show_axes=False):

        if manifold is None:
            manifold = self.manifold
        # for debugging purposes- does not affect functionality
        #-------------------------------------------------------------
        if manifold is 'sphere':

            raise NameError('the sphere manifold is not used\n\
            for the plot_cylinder method!\
            Use plot_sphere method instead!')

        if manifold not in ('sphere','cylinder'):
            raise NameError('{0} is not a recognized\n\
            manifold!'.format(manifold))
        #------------------------------------------------------------
        plt.figure()
        ax = plt.gca(projection='3d')
        #no need to change rstride,cstride,or linewidth
        #hence they are not given in the method header.
        ax.plot_surface(cylinder_surface[0],
                        cylinder_surface[1],
                        cylinder_surface[2],
                        rstride=1, cstride=1, linewidth=0,
                        antialiased=antialiased, color=color, alpha=alpha)
        if has_title:
            plt.title('Surface Plot: Finite Cylinder')

        ax.set_aspect('equal')
        ax.view_init(azim=-0.0005)
        ax.set_xlim(-self.height_cylinder,self.height_cylinder)
        ax.set_ylim(-self.height_cylinder,self.height_cylinder)
        ax.set_zlim(-self.height_cylinder,self.height_cylinder)
        ax.set_xticks([-self.height_cylinder,0,self.height_cylinder])
        ax.set_yticks([-self.height_cylinder,0,self.height_cylinder])
        ax.set_zticks([-self.height_cylinder,0,self.height_cylinder])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        if show_axes is False:
            ax.set_axis_off()
        plt.show()
    #----------------------------------------------------------------------
