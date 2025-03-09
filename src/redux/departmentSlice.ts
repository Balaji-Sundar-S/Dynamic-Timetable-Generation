// src/redux/departmentSlice.ts
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

// Define the type for the department state
interface DepartmentState {
  selectedDepartments: string[];
}

// Initial state
const initialState: DepartmentState = {
  selectedDepartments: [],
};

// Create the slice
const departmentSlice = createSlice({
  name: "departments",
  initialState,
  reducers: {
    setSelectedDepartments: (state, action: PayloadAction<string[]>) => {
      state.selectedDepartments = action.payload;
    },
  },
});

// Export actions and reducer
export const { setSelectedDepartments } = departmentSlice.actions;
export default departmentSlice.reducer;