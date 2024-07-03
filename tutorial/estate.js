class RealEstateInvestment {
    constructor(
      propertyId,
      address,
      propertyType,
      purchasePrice,
      estimatedValue,
      monthlyRent,
      monthlyExpenses,
      mortgageDetails,
      downPayment = 0.3 // Default to 30% down payment
    ) {
      this.propertyId = propertyId;
      this.address = address;
      this.propertyType = propertyType;
      this.purchasePrice = purchasePrice;
      this.estimatedValue = estimatedValue;
      this.monthlyRent = monthlyRent;
      this.monthlyExpenses = monthlyExpenses;
      this.mortgageDetails = mortgageDetails || {};
      this.downPayment = downPayment;
    }
  
    // You can define methods here to perform calculations (e.g., cash flow, ROI)
    calculateMonthlyPayment() {
      // Consider using a separate module or library for loan payment calculations
      const principal = this.purchasePrice * (1 - this.downPayment);
      // Implement logic to calculate monthly payment based on principal, interest rate (from mortgageDetails), and loan term (potentially 12 months for this scenario)
    }
  
    calculateTotalInvestment() {
      const downPaymentAmount = this.purchasePrice * this.downPayment;
      return downPaymentAmount + this.calculateMonthlyPayment() * 12; // Assuming 12 months of payments
    }
  }
      