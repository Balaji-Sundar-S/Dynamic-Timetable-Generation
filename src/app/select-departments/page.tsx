import DepartmentsTable from "@/components/ui/ui/departmentstable";

export default function Home() {
    return (
        <div className="flex flex-col items-center mt-[15%]">
            <p className="text-xl font-bold text-blue-800">Enter departments</p>
            <DepartmentsTable/>
        </div>
    );
  }