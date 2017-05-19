/**
 * Created by Jonny on 2017/5/12.
 */
function add_user() {
    add_user_mask.style = "display:block";
    add_user_box.style = "display:block";
}
close.onclick = function () {
    add_user_mask.style = "display:none";
    add_user_box.style = "display:none";
    owner.value="";
    user.value="";
    password.value="";
    remarks.value="";
};
cancel.onclick = function () {
    add_user_mask.style = "display:none";
    add_user_box.style = "display:none";
    owner.value="";
    user.value="";
    password.value="";
    remarks.value="";
};
function delete_box(user_id) {
    determine_box1.style = "display:block";
    determine_box2.style = "display:block";
    ids = user_id;
    user_ids = "#"+user_id
}
determine_close.onclick = function () {
    determine_box1.style = "display:none";
    determine_box2.style = "display:none";
};
determine_button.onclick = function () {
    determine_box1.style = "display:none";
    determine_box2.style = "display:none";
    $.ajax({
        url:"/del_user",
        type:"POST",
        data:{user_id:ids},
        success: function(){
            $(user_ids).remove()
  }});
};
function update_box(id,owner,user,password,remarks) {
    upd_owner.value = owner;
    upd_user.value = user;
    upd_password.value = password;
    upd_remarks.value = remarks;
    upd_id.value = id;
    upd_user_mask.style = "display:block";
    upd_user_box.style = "display:block";
}
upd_submit.onclick = function () {
    upd_user_mask.style = "display:none";
    upd_user_box.style = "display:none";
};
upd_close.onclick = function () {
    location.reload();
    upd_user_mask.style = "display:none";
    upd_user_box.style = "display:none";
};
upd_cancel.onclick = function () {
    location.reload();
    upd_user_mask.style = "display:none";
    upd_user_box.style = "display:none";
};