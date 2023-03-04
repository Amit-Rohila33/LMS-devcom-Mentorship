import { Component } from '@angular/core';
import {
  AbstractControl,
  AbstractControlOptions,
  FormBuilder,
  FormControl,
  FormGroup,
  ValidationErrors,
  ValidatorFn,
  Validators,
} from '@angular/forms';
import { User, UserType } from '../models/models';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
  hide = true;
  responseMsg: string = '';
  registerForm: FormGroup;

  constructor(private fb: FormBuilder, private api: ApiService) {
    //Input from user is taken using here
    this.registerForm = fb.group(
      {
        name: fb.control('', [Validators.required]),
        email: fb.control('', [Validators.required, Validators.email]),
        password: fb.control('', [
          Validators.required,
          Validators.minLength(8),
          Validators.maxLength(15),
        ]),
        password2: fb.control(''),
      },
      {
        validators: [repeatPasswordValidator],
      } as AbstractControlOptions
    );
  }
//Function that uses the input data to register the user
  register() {
    let user: User = {
      id: 0,
      name: this.registerForm.get('name')?.value,
      email: this.registerForm.get('email')?.value,
      user_type: UserType.STUDENT,
      password: this.registerForm.get('password')?.value,
    };
    this.api.createAccount(user).subscribe({
      next: (res: any) => {
        console.log(res);
        this.responseMsg = res.toString();
      },
      error: (err: any) => {
        console.log('Error: ');
        console.log(err);
      },
    });
  }
//To get correct appropriate format of data, the errors are defined below
  getNameErrors() {
    if (this.Name.hasError('required')) return 'Field is requied!';
    return '';
  }
  getEmailErrors() {
    if (this.Email.hasError('required')) return 'Email is required!';
    if (this.Email.hasError('email')) return 'Email is invalid.';
    return '';
  }
  getPasswordErrors() {
    if (this.Password.hasError('required')) return 'Password is required!';
    if (this.Password.hasError('minlength'))
      return 'Minimum 8 characters are required!';
    if (this.Password.hasError('maxlength'))
      return 'Maximum 15 characters are required!';
    return '';
  }
//Functions used to save the input data to FormControl
  get Name(): FormControl {
    return this.registerForm.get('name') as FormControl;
  }
  get Email(): FormControl {
    return this.registerForm.get('email') as FormControl;
  }
  get Password(): FormControl {
    return this.registerForm.get('password') as FormControl;
  }
  get RPassword(): FormControl {
    return this.registerForm.get('password2') as FormControl;
  }
}

// Validation function to ensure that password and repeat password match each other and then create an account
export const repeatPasswordValidator: ValidatorFn = (
  control: AbstractControl
): ValidationErrors | null => {
  const pwd = control.get('password')?.value;
  const rpwd = control.get('password2')?.value;
  if (pwd === rpwd) {
    control.get('password2')?.setErrors(null);
    return null;
  } else {
    control.get('password2')?.setErrors({ password2: true });
    return { password2: true };
  }
};
