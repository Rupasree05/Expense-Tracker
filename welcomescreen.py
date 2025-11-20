import streamlit as st
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Image } from 'react-native';

export default function WelcomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Image
          source={require(C:/Users/User/Desktop/Rupa Sree/expense_Tracker_Image.png)} // your logo image
          style={styles.logo}
        />

        <Text style={styles.title}>Smart Expense</Text>
        <Text style={styles.subtitle}>
          Track your spending.{"\n"}Grow your savings.
        </Text>

        <TouchableOpacity
          style={styles.button}
          onPress={() => navigation.navigate("Home")}
        >
          <Text style={styles.buttonText}>Get Started</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#D6EDFF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  content: {
    alignItems: 'center',
  },
  logo: {
    width: 90,
    height: 90,
    marginBottom: 25,
  },
  title: {
    fontSize: 28,
    fontWeight: '700',
    color: '#2C3E50',
  },
  subtitle: {
    fontSize: 16,
    color: '#4A4A4A',
    textAlign: 'center',
    marginVertical: 15,
    lineHeight: 22,
  },
  button: {
    backgroundColor: '#2E86DE',
    paddingVertical: 12,
    paddingHorizontal: 40,
    borderRadius: 50,
    marginTop: 20,
    elevation: 3,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
    fontWeight: '600',
  },
});
