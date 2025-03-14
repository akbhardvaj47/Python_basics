import React from 'react';
import { Button, SafeAreaView, Alert, View } from 'react-native';

export default function App() {
  const sendEmergencyAlert = () => {
    // In a real app, you'd send a request to your server here
    Alert.alert('Emergency Alert', 'SOS alert sent to emergency contacts!');
  };

  return (
    <SafeAreaView style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <View>
        <Button title="Send SOS" onPress={sendEmergencyAlert} />
      </View>
    </SafeAreaView>
  );
}
