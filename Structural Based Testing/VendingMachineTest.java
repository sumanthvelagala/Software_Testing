package com.example;

import static org.junit.Assert.*;
import org.junit.Test;

public class VendingMachineTest {

    @Test
    public void testExactPaymentCandy() {
        assertEquals("Item dispensed.", VendingMachine.dispenseItem(20, "candy"));
    }

    @Test
    public void testExactPaymentCoke() {
        assertEquals("Item dispensed.", VendingMachine.dispenseItem(25, "coke"));
    }

    @Test
    public void testExactPaymentCoffee() {
        assertEquals("Item dispensed.", VendingMachine.dispenseItem(45, "coffee"));
    }

    @Test
    public void testOverpaymentCandy() {
        assertEquals("Item dispensed and change of 30 returned", VendingMachine.dispenseItem(50, "candy"));
    }

    @Test
    public void testInsufficientFundsCandy() {
        assertEquals("Item not dispensed, missing 5 cents. Cannot purchase item.", VendingMachine.dispenseItem(15, "candy"));
    }

    @Test
    public void testInsufficientFundsCoke() {
        assertEquals("Item not dispensed, missing 3 cents. Can purchase candy.", VendingMachine.dispenseItem(22, "coke"));
    }

    @Test
    public void testInsufficientFundsCoffee() {
        assertEquals("Item not dispensed, missing 15 cents. Can purchase candy or coke.", VendingMachine.dispenseItem(30, "coffee"));
    }
}
