<template>
  <div class="home">
    <section class="">
      <div class="has-text-centered">
        <p class="title">Currencies:</p>
      </div>
    </section>
    <div class="columns is-mulytyline">
      <div class="column is-2">
        <div class="box hero has-text-centered mb-6">
          <h3 class="is-size-4">New Currency:</h3>
          <input 
          v-model="newCurr"
          type="text"
          class="input"
          
          >
          <button class="button" @click="addCurr">add</button>
        </div>
      </div>
      <div 
        class="column is-2" 
        v-for="currency in currencylist"
        :key="currency.id"
        @click="selectCurrency(currency)"
      >
        <div 
          :class="selectedcurrency == currency ? 'is-primary' : ''"
          class="box hero has-text-centered mb-6">
          <h3 class="is-size-3">{{ currency.name }}</h3>
          <button class="button">del</button>
        </div>
      </div>
    </div>
    <div v-if="selectedcurrency">
      <div 
        class="columns is-mulytyline"
        v-for="rate in selectedrates"
        :key="rate.id"
      >
        <h3 class="column is-2">{{ rate.date }} | {{ rate.rate }}</h3>
      </div>
      <input 
        v-model="date"
        type="text"
        class="input"
        style="width: 15%"
      >
      <input 
        v-model="rate"
        type="text"
        class="input"
        style="width: 15%"
      >
      <button 
      @click="addRate"
      class="button">
      Add
      </button>
      <div class="notification is-danger" v-if="errors.length">
      <p 
        v-for="error in errors"
        :key="error"
        >{{ error }}</p>
    </div>
      <ul class="graph">
        <li
          v-for="(bar, idx) in barheight"
          :key="idx"
          :style="{ height: bar+'%' }"
          class="graph-bar">
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Home',

    data() {
      return {
        currencylist: [],
        rateslist: [],
        selectedcurrency: null,
        selectedrates: [],
        date: null,
        rate: null,
        errors: [],
        newCurr: null,
        barheight: [],
      }
    },

    components: {
    },

    mounted() {
      this.getCurrencyList()
      this.getRatesList()
    },

    methods: {
      getCurrencyList() {
        axios
          .get('/api/v1/currencies/')
          .then(response => {
            this.currencylist = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

      getRatesList() {
        axios
          .get('/api/v1/rates/')
          .then(response => {
            this.rateslist = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

      selectCurrency(cur) {
        this.selectedcurrency = cur
        this.selectedrates = []
        this.barheight = []
        this.rateslist.forEach(rate => {
          if (rate.currency == cur.id) {
            this.selectedrates.push(rate)
            this.barheight.push(rate['rate'])
          }
        });
        var max = Math.max(...this.barheight)
        this.barheight = this.barheight.map( function(bar) {
          return (bar / max)*70
        });
        console.log(this.barheight)
        
      },

      addCurr() {
        this.errors = []

        const curr = {
          name: this.newCurr
        }
        axios
          .post('/api/v1/currencies/', curr)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            if (error.response['data']['name']) this.errors.push(...error.response['data']['name']) 
          })
      },

      addRate() {
        this.errors = []

        const rate = {
          currency: this.selectedcurrency['id'],
          date: this.date,
          rate: parseFloat(this.rate)
        }
        axios
          .post('/api/v1/rates/', rate)
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            if (error.response['data']['date']) this.errors.push(...error.response['data']['date'])
            if (error.response['data']['rate']) this.errors.push(...error.response['data']['rate']) 
          })
        this.getCurrencyList()
        this.getRatesList()
      },
    }
  }
</script>


<style lang="scss">
  .graph {
    display: block;
    background-color: gray;
    width: 85%;
    height: 300PX;
  }

  .graph-bar {
    display: inline-block;
    width: 3%;
    background-color: blue;
    margin: 3px;
    margin-top: 5%;
  }
</style>