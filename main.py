def toh(n, src, hlp, des):
	if n == 1:
		print("Move Disk ", n, "from rod ", src, "to rod ", des)
		return
	toh(n - 1, src, des, hlp)
	print("Move Disk ", n, "from rod ", src, "to rod ", des)
	toh(n - 1, hlp, src, des)


def main():
	n = int(input("Enter the number of disk: "))
	src, hlp, des = 1, 2, 3
	toh(n, src, hlp, des)
	print("Total Steps Required for this Tower of Hanoi is: ", pow(2, n) - 1)


if __name__ == "__main__":
	main()
