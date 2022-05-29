import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CollectionListComponent } from './components/collection-list/collection-list.component';

const routes: Routes = [
  { path: '', redirectTo: 'app', pathMatch: 'full' },
  { path: 'app', component: CollectionListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }