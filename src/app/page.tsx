'use client'

import React from "react";
import Image from "next/image";
import { Input } from "@/components/ui/ui/input";
import { Button } from "@/components/ui/ui/button";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();
  const handleSubmit=()=>{
    router.push("/select-departments")
  }
  return (
    <div className="flex flex-col items-center mt-[15%]">
      <p className="text-xl font-bold text-blue-800">Login</p>
      <Input required className="w-96 mt-10" placeholder="Enter your email"/>
      <Input required className="w-96 mt-5" placeholder="Enter your password"/>
      <Button type="submit" className="mt-10 bg-blue-800" onClick={()=>{handleSubmit()}}>Submit</Button>
    </div>
  );
}
