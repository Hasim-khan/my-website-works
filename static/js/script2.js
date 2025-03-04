function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.querySelector('.toggle-btn');
    
    sidebar.classList.toggle('open');
    toggleBtn.classList.toggle('active');
  }
  