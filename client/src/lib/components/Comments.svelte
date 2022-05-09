<script>
    import SettingsController from "./../SettingsController"  
    
    let settings = new SettingsController()
    let colorTheme = settings.getJson().colorTheme

    let comments = []
    
    function createNewComment() {
        let text = document.getElementById("newComment").value
        text = text.replace(/\n\r?/g, '<br />')
        let textHtml = document.createElement('div');
        textHtml.innerHTML = text
        const username = "username"
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        let time = mm + '.' + dd + '.' + yyyy;

        let comment = {username:username,time:time,text:textHtml}
        
        comments = [...comments, comment]
        console.log(comments);
    }
</script>

<div class="commentSection">
    {#each comments as comment}
        <div class="comment">
            <div class="username">{comment.username}  <span class="commentDate">Commented on {comment.time} </span></div>
            <p>{comment.textHtml} </p>
        </div>
    {/each}

    <div class="form-group">
        <textarea class="form-control commentTextarea" id="newComment" rows="3"></textarea>
        <button type="submit" class="btn btn-primary mb-2 commentButton" on:click={createNewComment}>Comment</button>
    </div>
</div>

