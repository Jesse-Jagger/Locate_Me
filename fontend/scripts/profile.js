document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('profileForm').addEventListener('submit', function(event) {
        event.preventDefault();
        // Add AJAX request to update profile information here
        alert('Profile updated successfully!');
    });

    document.getElementById('changePasswordForm').addEventListener('submit', function(event) {
        event.preventDefault();
        // Add AJAX request to change password here
        alert('Password changed successfully!');
    });

    document.getElementById('uploadProfilePicture').addEventListener('change', function(event) {
        const reader = new FileReader();
        reader.onload = function() {
            document.getElementById('profilePicture').src = reader.result;
        }
        reader.readAsDataURL(event.target.files[0]);
    });
});