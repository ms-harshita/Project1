
from flask import Flask,redirect, url_for, request, render_template

app=Flask(__name__)


import boto as routers
@app.route('/')
def route():
    return render_template("index.html")

@app.route('/homeEC2/',methods=['GET'])
def home1():
    return render_template("homeEC2.html")


@app.route('/homeS3/',methods=['GET'])
def home2():
    return render_template("homeS3.html")   


@app.route('/createS3/')
def create_s3_bucket():
    return render_template("createS3.html")



@app.route('/createdS3/', methods=["POST"])
def created_s3_bucket():
    if request.method == "POST":
        s3bucket_id= request.form["s3bucket_id"]
        routers.create_bucket(s3bucket_id)
        return redirect(url_for("success"))



@app.route('/deleteS3/')
def delete_s3_bucket():
    return render_template("deleteS3.html")


@app.route('/deletedS3/', methods=["POST"])
def deleted_s3_bucket():
    if request.method == "POST":
        s3bucketdelete_id= request.form["s3bucketdelete_id"]
        routers.delete_bucket(s3bucketdelete_id)
        return redirect(url_for("success"))

@app.route('/bucketlistS3/')
def listbucket():
    list3=routers.list_bucket()
    return render_template("bucketlistS3.html",list3=list3)


@app.route('/create_ec2/')
def create_ec2():
    routers.create_instance()
    return render_template("success.html")




@app.route('/success')
def success():
    return render_template("success.html")  

@app.route('/terminateEC2/')
def terminates_ec2():
    return render_template("terminateEC2.html")      
 
@app.route('/terminatedEC2/', methods=["POST"])
def terminated_ec2():
    if request.method == "POST":
        tid=request.form["terminate_id"]

        routers.terminate_ec2(tid)
        return redirect(url_for("success"))
       


@app.route('/stopEC2/')
def stop_ec2():
    return render_template("stopEC2.html")

@app.route('/stopEC2/', methods=["POST"])
def stopped_ec2():
    if request.method == "POST":
        stop_id= request.form["stop_id"]
        routers.stop_ec2(stop_id)
        return redirect(url_for("success"))
       
@app.route('/startEC2/')
def start_ec2():
    return render_template("startEC2.html")

    
@app.route('/startEC2/', methods=["POST"])
def started_ec2():
    if request.method == "POST":
        start_id= request.form["start_id"]
        routers.start_ec2(start_id)
        return redirect(url_for("success"))
        

 
    

if __name__=='__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port) 


