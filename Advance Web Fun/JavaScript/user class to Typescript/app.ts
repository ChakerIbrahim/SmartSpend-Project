class User {
  private firstName: string;
  private lastName: string;
  private address: string;
  private phoneNumber: string;

  constructor(
    firstName: string,
    lastName: string,
    address: string,
    phoneNumber: string
  ) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.address = address;
    this.phoneNumber = phoneNumber;
  }

  // Getters
  public getFirstName(): string {
    return this.firstName;
  }

  public getLastName(): string {
    return this.lastName;
  }

  public getAddress(): string {
    return this.address;
  }

  public getPhoneNumber(): string {
    return this.phoneNumber;
  }

  // Setters
  public setFirstName(fName: string): void {
    this.firstName = fName;
  }

  public setLastName(lName: string): void {
    this.lastName = lName;
  }

  public setAddress(address: string): void {
    this.address = address;
  }

  public setPhoneNumber(phone: string): void {
    this.phoneNumber = phone;
  }
}

const user1 = new User(
  "Jalil",
  "Wasaya",
  "Ramallah",
  "0597121488"
);
console.log(user1.getFirstName());   
console.log(user1.getLastName());    
console.log(user1.getAddress());     
console.log(user1.getPhoneNumber()); 

user1.setFirstName("Ahmad");
user1.setLastName("Ali");
user1.setAddress("Jerusalem");
user1.setPhoneNumber("0560000000");

console.log(user1.getFirstName());   
console.log(user1.getLastName());    
console.log(user1.getAddress());     
console.log(user1.getPhoneNumber()); 
