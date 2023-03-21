import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageAuthorComponent } from './manage-author.component';

describe('ManageAuthorComponent', () => {
  let component: ManageAuthorComponent;
  let fixture: ComponentFixture<ManageAuthorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ManageAuthorComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ManageAuthorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
