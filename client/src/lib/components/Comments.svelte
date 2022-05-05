<script>
    let comments = []
    
    function createNewComment() {
        let text = document.getElementById("newComment").value
        text = text.replace(/\n\r?/g, '<br />')
        const username = "username"
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        let time = mm + '.' + dd + '.' + yyyy;

        let comment = {username:username,time:time,text:text}
        
        comments = [...comments, comment]
        console.log(comments);
    }
</script>

<div class="commentSection">
    {#each comments as comment}
        <div class="comment">
            <div class="username">{comment.username}  <span class="commentDate">Commented on {comment.time} </span></div>
            <p>{comment.text} </p>
        </div>
    {/each}

    <div class="form-group">
        <textarea class="form-control commentTextarea" id="newComment" rows="3"></textarea>
        <button type="submit" class="btn btn-primary mb-2 commentButton" on:click={createNewComment}>Comment</button>
    </div>
</div>

