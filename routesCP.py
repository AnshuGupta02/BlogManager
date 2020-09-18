from appCP import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
import formCP
from modelsCP import Task
from datetime import datetime



@app.route('/')
@app.route('/home')   #get to default hota hai, post add krne k lye list bnao
def home():
    tsks=Task.query.all()
    return render_template('home.html', page='MY BLOGS', tasks=tsks)



@app.route('/add', methods=['GET','POST'])
def add():
    fms=formCP.AddText()
    if fms.validate_on_submit():
        t=Task(title=fms.title.data, date=datetime.now(), blog=fms.blog.data)
        db.session.add(t)
        db.session.commit()
        flash('Blog added to your database')
        return redirect(url_for('home'))
    return render_template('add.html', page='ADD BLOG', form=fms)



@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task=Task.query.get(task_id)
    form=formCP.AddText()
    if task:
        if form.validate_on_submit():
            task.title=form.title.data
            task.blog=form.blog.data
            task.date= datetime.now()
            db.session.commit()
            flash('Blog has been updated')
            return redirect(url_for('home'))
        form.title.data= task.title
        form.blog.data= task.blog
        return render_template('edit.html', form=form, task_id=task_id, page='EDIT BLOG')
    else:
        flash('Blog not found')
    return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task=Task.query.get(task_id)
    form=formCP.DeleteText()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash("Blog has been Deleted")
            return redirect(url_for('home'))
        return render_template('delete.html', page='DELETE BLOG', form=form, task_id=task_id, title=task.title)
    else:
        flash('Blog not found')
    return redirect(url_for('home'))


