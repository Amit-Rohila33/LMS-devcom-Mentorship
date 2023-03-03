import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageGenreComponent } from './manage-genre.component';

describe('ManageGenreComponent', () => {
  let component: ManageGenreComponent;
  let fixture: ComponentFixture<ManageGenreComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ManageGenreComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ManageGenreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
