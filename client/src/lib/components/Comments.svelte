<script>
    let comments = []
    
    function createNewComment() {
        const text = document.getElementById("newComment").value
        const username = "username"
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        let time = mm + '.' + dd + '.' + yyyy;

        let comment = {username:username,time:time,text:text}
        
        comments=[...comments, comment]
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
        <textarea class="form-control" id="newComment" rows="3"></textarea>
        <button type="submit" class="btn btn-primary mb-2" on:click={createNewComment}>Comment</button>
      </div>

    
</div>

<style>
.comment{
    
    border-bottom: 1px solid gray;

}
.username{
    font-size: 20px;
    color: rgb(124, 0, 173);
}
.commentDate{
    font-size: 10px;
    color: gray;
}
</style>