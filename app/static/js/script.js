
// new post
// const toggleCreatePost = function(){
//     document.getElementById('createpost').click();
// }

//check js

// like and dislike logic
$(document).ready(function() {
    $('.like').click(toggleLike);
    $('.commentform').submit(createComment);
})


// const toggleLike = e => {
//    const user_id = $('.user_id').attr('id');
//   if (user_id) {
//     const [like, post_id] = e.currentTarget.id.split(' ')
//     return postLike(post_id.slice(-1), like)    
//   }
//   return false;
// }

// const postLike = (post_id, like)  => {
//   const likes = $(`.count-likes${post_id}`);
//   const url = `/post/${like}/${post_id}`;
//   $.post(url, function (data) {
//   likes.text(data[0])
//   console.log(likes);
//   })
// }

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