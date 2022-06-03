import { Component, OnInit } from '@angular/core';
import { Blockchain } from 'app/models/blockchain.model';
import { Collection } from 'app/models/collection.model';
import { Nft } from 'app/models/nft.model';
import { CollectionserviceService } from 'app/services/collectionservice.service';


import * as Highcharts from 'highcharts';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  collection?: Collection[];
  blockchain?: Blockchain[];
  nft?: Nft[];
  
  selectedBlockchain = '';
  selectedCollection = '';

  

  constructor(private collectionserviceService: CollectionserviceService) { }
  
  ngOnInit() {
    
   this.retrieveBlockchain();
   Highcharts.chart('container', this.options);
   //this.createChartLine();
  }

  

  retrieveBlockchain(): void {
    this.collectionserviceService.getAllBlockchains().subscribe(
      (data) => {
        this.blockchain = data;
        console.log(data);
        
      },
      (error) => {
        console.log(error);
      }
    );
  }

  onSelectBlockchain(value: any){
    console.log(value);
    this.searchCollections();
  }
  onSelectCollection(value: any){
    console.log(value);
    this.searchNfts();
  }

  

  searchCollections(): void {
    // this.currentCollection = {};
     //this.currentIndex = -1;
 
     this.collectionserviceService.findByBlockchain(this.selectedBlockchain).subscribe(
       (data) => {
         this.collection = data;
         console.log(data);
       },
       (error) => {
         console.log(error);
       }
     );
   } 

   searchNfts(): void {
    // this.currentCollection = {};
     //this.currentIndex = -1;
 
     this.collectionserviceService.findByCollection(this.selectedCollection).subscribe(
       (data) => {
         this.nft = data;
         console.log(data);
       },
       (error) => {
         console.log(error);
       }
     );
   } 



  
  public options: any = {
    chart: {
       type: 'bar'
    },
    accessibility: {
        description: '',
    },
    title: {
       text: 'Historic World Population by Region'
    },
    subtitle: {
        text: 'Sources: Dummy data'
    },
    xAxis: {
        categories: ['Africa', 'America', 'Asia', 'Europe', 'Oceania'],
        tickmarkPlacement: 'on',
        title: {
            enabled: false
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Population (millions)',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        valueSuffix: ' millions'
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: -40,
        y: 80,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
        shadow: true
    },
    series: [{
        name: 'Year 1800',
        data: [107, 31, 635, 203, 2]
    }, {
        name: 'Year 1900',
        data: [133, 156, 947, 408, 6]
    }, {
        name: 'Year 2000',
        data: [814, 841, 3714, 727, 31]
    }, {
        name: 'Year 2016',
        data: [1216, 1001, 4436, 738, 40]
    }]
  }
  
  
  

}
