from flask import Flask,render_template,request

from utils import snowflakes
from helpers import video_authors_list
from utils import top50details
from utils import comments_util 
from helpers import s3_downloader

app=Flask(__name__)


ctx,cs=snowflakes.main()
authors_list=video_authors_list.read_snowflakes(cs)


@app.route('/homepage')
def homepage():
    return render_template ('homepage.html',authors=authors_list)


@app.route('/krishtop3',methods=['POST'])
def krishtop3():
    author_name=authors_list[0][0]
    top_details=top50details.top50_snowflakes(cs,author_name)
    all_thumbnails=top50details.main(top_details)
    # print(all_thumbnails)
    zipped=zip(top_details,all_thumbnails)
    return render_template('top50.html',details=zipped)
    

@app.route('/mysirgtop3',methods=['POST'])
def mysirgtop3():
    author_name=authors_list[1][0]
    top_details=top50details.top50_snowflakes(cs,author_name)
    all_thumbnails=top50details.main(top_details)
    zipped=zip(top_details,all_thumbnails)
    return render_template('top50.html',details=zipped)

@app.route('/hiteshtop3',methods=['POST'])
def hiteshtop3():
    author_name=authors_list[2][0]
    top_details=top50details.top50_snowflakes(cs,author_name)
    all_thumbnails=top50details.main(top_details)
    zipped=zip(top_details,all_thumbnails)
    return render_template('top50.html',details=zipped)

@app.route('/teluskotop3',methods=['POST'])
def teluskotop3():
    author_name=authors_list[3][0]
    top_details=top50details.top50_snowflakes(cs,author_name)
    all_thumbnails=top50details.main(top_details)
    zipped=zip(top_details,all_thumbnails)
    return render_template('top50.html',details=zipped)
    
    
@app.route('/comments',methods=['POST'])
def comments():
        video_id=request.form.get('vid_id')
        print(video_id)
        final_comments=comments_util.main(video_id)
        return render_template('comments_print.html',comments=final_comments)
    
@app.route('/download',methods=['POST'])
def download():
    title=request.form.get('download_title')
    s3_downloader.s3_connector(title+'.3gpp')
    return render_template('download_completed.html')
    

    
if __name__=='__main__':
    app.run(debug=True)