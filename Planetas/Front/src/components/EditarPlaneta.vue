<template>
  <div class="universe-container">
    <h1>Editar Planeta</h1>
    <div class="planet-container">
      <form @submit.prevent="editarPlaneta" class="planet-item">
        <div class="input-group">
          <label for="nome">Nome:</label>
          <input type="text" id="nome" v-model="planeta.nome" placeholder="Nome do Planeta" required>
        </div>
        <div class="input-group">
          <label for="temperatura">Temperatura Média</label>
          <input type="number" id="temperatura" v-model="planeta.temperatura_media" placeholder="Temperatura Média" required>
        </div>
        <div class="input-group">
          <label for="ano">Ano da descoberta</label>
          <input type="text" id="ano" v-model="planeta.ano" placeholder="Ano da descoberta" required>
        </div>
        <div class="input-group">
          <label for="rotacao">Rotação:</label>
          <input type="text" id="rotacao" v-model="planeta.rotacao" placeholder="Rotação do Planeta" required>
        </div>
        <div class="input-group">
          <label for="translacao">Translação:</label>
          <input type="text" id="translacao" v-model="planeta.translacao" placeholder="Translação do Planeta" required>
        </div>
        <button class="action-button" type="submit">Salvar</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      planeta: {
        id: null,
        nome: '',
        temperatura:'',
        ano:'',
        rotacao: '',
        translacao: ''
      }
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
    },
    async editarPlaneta() {
      try {
        await axios.put(`http://localhost:8000/api/v1/planetas/${this.planeta.id}`, this.planeta);
        
        this.$router.push('/listar-todos');

        window.alert("Planeta salvo com sucesso!" )
      } catch (error) {
        console.error('Erro ao editar planeta:', error);
      }
    }
  }
};
</script>

<style>
  *{
    margin: 0;
    padding: 0;
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
    padding: 60px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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

  .input-group {
    margin-bottom: 20px;
  }

  .input-group label {
    display: block;
    margin-bottom: 5px;
  }

  .input-group input {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 10px;
    font-size: 16px;
  }

</style>