def simul_pipeline():
    def __init__(self):
        pathToRefPath = rospy.get_param("map_dir")
        self.refPath = setReferencePath()


def setReferencePath(self, pathToRefPath):
        # Read YAML file
        with open(pathToRefPath, 'r') as file:
            points = yaml.safe_load(file)

            #Save in numpy array
            points = np.array([v for v in points['reference_path']])

        return points