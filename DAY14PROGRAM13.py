class point:
    def __init__(rohith,x=0,y=0):
        rohith.x=x
        rohith.y=y
    def __del__(rohith):
        class_name=rohith.__class__.__name__
        print(class_name,"destroyed")
