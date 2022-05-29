import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { NFTsales } from '../models/nftsales.model';
import { Blockchain } from '../models/blockchain.model';
import { Collection } from '../models/collection.model';
import { Nft } from '../models/nft.model';
import { Currency } from '../models/currency.model';

const baseUrl = 'http://localhost:8000/api/collections';
@Injectable({
  providedIn: 'root'
})
export class CollectionserviceService {
  constructor(private http: HttpClient) { }
  getAllCollection(): Observable<Collection[]> {
    return this.http.get<Collection[]>(baseUrl);
  }
  
  findByBlockchain(blockchain: any): Observable<Collection[]> {
    return this.http.get<Collection[]>(`${baseUrl}?blockchain=${blockchain}`);
  }
}
