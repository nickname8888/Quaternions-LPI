def post(plate):
        from firebase import firebase
        FBconn = firebase.FirebaseApplication('https://lip-demo-default-rtdb.firebaseio.com/',None)
        data = {"numberplate":plate}
        result = FBconn.post('/mMyTestPlate/',data)
        print(result)
