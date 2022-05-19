document.getElementById('postcomms').addEventListener('click', makeComment);
function makeComment(){
    alert("Please kill me")
}

// new post
const toggleCreatePost = function(){
    document.getElementById('createpost').click();
}

//check js

// like and dislike logic
$(document).ready(function() {
    $('.likes').click(toggleLike);
    $('.commentform').submit(createComment);
})

// const resetForm = function(){
//     document.getElementById('contactForm').reset();
// }

// document.getElementById('sendBtn').addEventListener('click', clickedBtn);
// function clickedBtn(){
//     confirm('Do you want to send this message?')
// }

// document.getElementById('commentbtn').addEventListener('click', clicked);
// function clicked(){
//     // Confirm("You clicked the button!");
//     confirm('Do you want?')
// }


const toggleLike = event => {
    const user_id = $('.user_id').attr('id')
    if (user_id) {
        const[like, post_id] = event.currentTarget.id.split(' ')
        return likesDislikes(post_id.slice(-1),like)
    }
    return alert('You must be logged in to like or dislike a post')
}

const likesDislikes = (post_id, like) => {
    const likes = $(`.total-likes${post_id}`);
    const dislikes = $(`.total-dislikes${blog_id}`);
    const url = `/blog/${like}/${blog_id}`;
    $.post(url, function (data) {
        likes.text(data[0])
        dislikes.text(data[1])
    })

}

const createComment = event => {
    event.preventDefault()
    const post_id = event.currentTarget.id.slice(-1,12)
    const url = `/comment/${post_id}/add`
    const form = $('#commentForm' + post_id)
    const data = form.serialize()
    $.post(url, data, function (newComment) {
    const comment = `<p class="pl-3"><span class="badge badge-secondary custom-color">By @${newComment.user}</span> <small>${newComment.commentbody}</small></p>`
      $(`.comment-section${post_id}`).prepend(comment)
      return form.trigger('reset')
    } )
  }

// const postComment = comm => {
//     comm.preventDefault();
//     const post_id = comm.CurrentTarget.id.slice(-1,12)
//     const form = $('#commentForm' + post_id)
//     const comment = form.serialize()
//     const url ='/comments/' + post_id + '/newcomment'
//     $.post(url, comment, function(newComment){
//         const comment = `<div class="comment"><p>' + 
//         By @${newComment.user.username}</p>
//         <p>${newComment.comment}</p>
//         </div>`
//         $(`.comment-section${post_id}`).prepend(comment)
//             return form.trigger('reset')
//     })
// }
// } const comment = `<p class="pl-3"><span class="badge 
// badge-secondary custom-color">By @${newComment.user}</span> 
/* <small>${newComment.body}</small></p>` */
// $(`.comment-section${pitch_id}`).prepend(comment)
// return form.trigger('reset')
// } 