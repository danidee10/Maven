__author__ = 'danidee'

class level():

    def level_est(self, all_objects):
        for activity in all_objects:
            resource = activity.resource
            est = activity.est
            duration = activity.duration

            if est == 0:
                for count in range(duration):
                    activity.level[0].append(resource)
            else:
                while len(activity.level[0]) < est:
                        activity.level[0].append(0)

                for count in range(duration):
                    activity.level[0].append(resource)

    def level_lst(self, all_objects):
        for activity in all_objects:
            resource = activity.resource
            est = activity.est
            lst = activity.lst
            duration = activity.duration

            if est == lst:
                while len(activity.level[1]) < lst:
                    activity.level[1].append(0)

            elif est != lst:
                while len(activity.level[1]) < lst-1:
                    activity.level[1].append(0)

            for count in range(duration):
                activity.level[1].append(resource)

        return all_objects


if __name__ == '__main__': main()
