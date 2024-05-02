import { createRouter, createWebHistory } from 'vue-router'; // Importe as funções necessárias do Vue Router
import Home from '@/components/Home.vue';
import ListarTodos from '@/components/ListarTodos.vue';
import VisualizarPlaneta from '@/components/VisualizarPlaneta.vue';
import AdicionarPlaneta from '@/components/AdicionarPlaneta.vue';
import EditarPlaneta from '@/components/EditarPlaneta.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/listar-todos', component: ListarTodos },
  { path: '/visualizar/:id', component: VisualizarPlaneta },
  { path: '/adicionar', component: AdicionarPlaneta },
  { path: '/editar/:id', component: EditarPlaneta }
];


const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
