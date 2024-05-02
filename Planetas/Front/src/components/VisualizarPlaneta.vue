<template>
  <div class="universe-container">
    <h1>Detalhes do Planeta</h1>
    <div class="planet-container">
      <div class="planet-item">
      <h2>{{ planeta.nome }}</h2>
      <img :src="'https://scx2.b-cdn.net/gfx/news/hires/2015/whatsimporta.jpg'" alt="Imagem do Planeta" class="planet-image">
      <p>Temperatura Média: {{ planeta.temperatura_media }} °C</p>
      <p>Ano da descoberta: {{ planeta.ano }}</p>
      <p>Periodo de rotação: {{ planeta.rotacao }}</p>
      <p>Periodo de translação: {{ planeta.translacao }}</p>
      </div>
      
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      planeta: {}
    };
  },
  created() {
    this.fetchPlaneta();
  },
  methods: {
    async fetchPlaneta() {
      const planetaId = this.$route.params.id;
      try {
        const response = await axios.get(`http://localhost:8000/api/v1/planetas/${planetaId}`);
        this.planeta = response.data;
      } catch (error) {
        console.error('Erro ao buscar planeta:', error);
      }
    }
  }
};
</script>

<style scoped>
  body{
    margin: 0px;
    padding: 0px;
  }
  .universe-container {
    text-align: center;
    background-image: url('https://64.media.tumblr.com/d2e865fb75790082d43bf3d39ca0669a/0fb2249f70bd9ca0-a7/s400x600/b63cc2ecc28102c0fbafb40be0ecd388ca980de1.gif');
    background-size: 100;
    height: 100vh;
  }

  h1 {
    color:#fff;
    font-size: 3rem;
    padding: 90px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  h2 {
    color:#fff;
    margin-bottom: 60px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  p{
    margin-top: 7px;
  }

  .planet-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .planet-item {
    margin: 0 10px 20px;
    padding: 60px 20px;
    color: whitesmoke; 
    border: 2px solid whitesmoke;
    border-radius: 5px;
    text-align: center;
    background-color: transparent; 
    backdrop-filter: blur(2px);
  }

  .planet-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 10px;
  }

  
</style>