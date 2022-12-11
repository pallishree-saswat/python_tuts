from flask import request, render_template, redirect, flash, url_for
from datetime import date
from models.Post import *
from app import app

# routes


@app.route('/home')
def index():
    # get dat afrom db
    data = db.session.query(Post).order_by(Post.id.desc()).all()
    return render_template('index.html', posts=data)


@app.route('/add')
def addForm():
    return render_template('add.html')


@app.route('/create', methods=['POST'])
def createPost():
    print("inside create fun")
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        author = request.form['author']
        created_date = date.today()

        # save data to db
        Post.create({
            'title': title,
            'desc': desc,
            'author': author,
            'created_date': created_date
        })

        flash("Post created Successfully")
        return redirect(url_for('index'))


# get single post by id
@app.route('/single/<int:id>', methods=['GET'])
def singlePost(id):
    if request.method == 'GET':
      
        post = Post.query.get(id)
        return render_template('post.html', post=post)


# delete route
@app.route('/delete/<int:id>', methods=['GET'])
def deletePost(id):
    if request.method == 'GET':
        deleted_post = Post.query.get(id)
        db.session.delete(deleted_post)
        db.session.commit()
        flash("Deleted post successfully")
        return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET'])
def editPage(id):
    if request.method == 'GET':
        post = db.session.get(Post,id)
        return render_template('edit.html', post=post)
@app.route('/update', methods=['POST'])
def updatePost():
    if request.method == 'POST':
        #get post to be edit
        updated_post = Post.query.get(request.form['id'])

        #edit
        updated_post.title = request.form['title']
        updated_post.desc = request.form['desc']
        updated_post.author = request.form['author']
        db.session.commit()
        return redirect(url_for('index'))

        
