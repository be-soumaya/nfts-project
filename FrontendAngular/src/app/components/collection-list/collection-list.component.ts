import { Component, OnInit } from '@angular/core';

import { Collection } from 'src/app/models/collection.model';
import { CollectionserviceService } from 'src/app/services/collectionservice.service';

@Component({
  selector: 'app-collection-list',
  templateUrl: './collection-list.component.html',
  styleUrls: ['./collection-list.component.css']
})
export class CollectionListComponent implements OnInit {
  collection?: Collection[];
  currentCollection: Collection = {};
  currentIndex = -1;
  Blockchain= '';
   

  constructor(private collectionserviceService: CollectionserviceService) { }

  ngOnInit(): void {
    this.retrieveCollection();
  }

  retrieveCollection(): void {
    this.collectionserviceService.getAllCollection().subscribe(
      (data) => {
        this.collection = data;
        console.log(data);
      },
      (error) => {
        console.log(error);
      }
    );
  }

  refreshList(): void {
    this.retrieveCollection();
    this.currentCollection = {};
    this.currentIndex = -1;
  }
  setActiveCollection(collection: Collection, index: number): void {
    this.currentCollection = collection;
    this.currentIndex = index;
  }


  searchBlockchain(): void {
    this.currentCollection = {};
    this.currentIndex = -1;

    this.collectionserviceService.findByBlockchain(this.Blockchain).subscribe(
      (data) => {
        this.collection = data;
        console.log(data);
      },
      (error) => {
        console.log(error);
      }
    );
  }

}
