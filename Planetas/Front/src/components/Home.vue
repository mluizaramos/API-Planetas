<template>
    <div class="universe-container">
      <div class="universe-content">
        <h1>API DE PLANETAS E LUAS</h1>
        <router-link to="/listar-todos" class="link">LISTA DE PLANETAS</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePage'
  };
  </script>
  
  <style>
  *{
    margin:0;
    padding: 0;
  }

  .universe-container {
    background-image: url('https://cdn.pixabay.com/animation/2023/06/06/06/51/06-51-32-766_512.gif'); 
    background-position: center;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }
  
  .universe-content {
    text-align: center;
    color: #fff;
  }
  
  h1 {
    font-size: 4rem;
    margin-bottom: 20px;
    margin-bottom: 80px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  
  .link {
    border: 2px solid whitesmoke;
    background-color: transparent;
    padding: 10px 35px;
    color: white; 
    text-decoration: none;
    font-weight: bold;
    font-size: 20px;
    cursor: pointer;
    border-radius: 2px;
    transition: 0.3s ease;
    backdrop-filter: blur(300px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    
  }

  .link:hover {
    font-size: 22px;
    background-color: whitesmoke;
    color: #0c0d12
    
  }
  </style>
  