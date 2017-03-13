from spider.course import Course
from spider.flie_downloader import File_Downloader

if __name__ == '__main__':
    id = int(raw_input('Input your course id:'))

    course = Course(id)
    print "Your course's name is [" + course.name + "]"
    print "The following are the courses you will download:"
    for video in course.videos:
        print video['name']
    print "---------------------------------"
    file_downloader = File_Downloader(course.name, course.videos)

