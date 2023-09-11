import MuiLayout from "ui/Layout/MuiLayout";

export default function RootLayout({ children }: { children: React.ReactNode }) {
	return (
		<MuiLayout>
			<html lang="en">
				<body>{children}</body>
			</html>
		</MuiLayout>
	);
}
