import { createSlice } from "@reduxjs/toolkit";


const initialState={
    username:"",
    password:"",
    firstName:"",
    lastName:"",
    groupsList:[],
    loginStatus:false,
    admin:false,
}


export const UserSlice =createSlice({
    name:"user",
    initialState,
    reducers:{
        setUserProp:(state,action)=>{
            state[action.payload.prop]=action.payload.value;
        },
        cleanUserSlice:(state)=>{
            state.userId=""
            state.password=""
            state.firstName=""
            state.role=""
            state.groupsList=[]
            state.loginStatus=false
            state.admin=false
        }
    }
})

export const {setUserProp,cleanUserSlice} =UserSlice.actions
export default UserSlice.reducer