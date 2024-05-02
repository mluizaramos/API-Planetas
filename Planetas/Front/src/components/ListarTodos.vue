<template>
  <div class="universe-container">
    <h1>Lista de Planetas</h1>
    <router-link to="/adicionar" class="adicionar">+</router-link>

    <div class="planet-container">
      <div v-for="planeta in planetas" :key="planeta.id" class="planet-item">
        <img :src="'https://scx2.b-cdn.net/gfx/news/hires/2015/whatsimporta.jpg'" alt="Imagem do Planeta" class="planet-image">
        <h3>{{ planeta.nome }}</h3>
        <div class="button-container">
          <router-link :to="'/visualizar/' + planeta.id" class="action-button">Ver Detalhes</router-link>
          <router-link :to="'/editar/' + planeta.id" class="action-button">Editar</router-link>
          <button @click="excluirPlaneta(planeta)" class="action-button">Excluir</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      planetas: []
    };
  },
  created() {
    this.fetchPlanetas();
  },
  methods: {
    async fetchPlanetas() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/planetas');
        this.planetas = response.data;
      } catch (error) {
        console.error('Erro ao buscar planetas:', error);
      }
    },
    async excluirPlaneta(planeta) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/planetas/${planeta.id}`);
        this.planetas = this.planetas.filter(p => p.id !== planeta.id);
      } catch (error) {
        console.error('Erro ao excluir planeta:', error);
      }
    },
    editarPlaneta(planeta) {
      this.$router.push({ name: 'EditarPlaneta', params: { id: planeta.id } });
    },
    visualizarPlaneta(planeta) { 
      this.$router.push({ name: 'VisualizarPlaneta', params: { id: planeta.id } });
    }
  }
};
</script>

<style scoped>
  *{
    margin: 0;
    padding: 0;
  }

  .universe-container {
    text-align: center;
    background-image: url('https://64.media.tumblr.com/d2e865fb75790082d43bf3d39ca0669a/0fb2249f70bd9ca0-a7/s400x600/b63cc2ecc28102c0fbafb40be0ecd388ca980de1.gif');
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    
  }

  h1 {
  color: #fff;
  font-size: 3rem;
  padding: 50px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .adicionar {
  color: #fff;
  font-size: 3rem;
  padding: 0 90px 0 0;
  margin-left: auto;
  text-decoration: none;
  }

  .adicionar:hover{
    font-weight: bold;
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
    height: 90px;
    border-radius: 50%;
    margin-bottom: 10px;
  }

  .button-container {
    margin-top: 10px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .action-button {
    background-color: transparent; 
    color: whitesmoke; 
    border: 2px solid whitesmoke;
    padding: 10px 20px;
    margin: 5px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    text-decoration: none;
  }

  .action-button:hover {
    background-color: whitesmoke;
    color: #0c0d12
  }
</style>
