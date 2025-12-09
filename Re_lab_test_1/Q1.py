def push(stack, element):
	stack.append(element)


def pop(stack):
	if not stack:
		print("Stack is empty! Cannot pop.")
		return None
	return stack.pop()


def display(stack):
	print("Current stack (top on right):", stack)


def main():
	stack = []

	# Push 5 elements
	for value in [10, 20, 30, 40, 50]:
		push(stack, value)
	print("After pushing 5 elements:")
	display(stack)

	# Pop 2 elements
	print("\nPopping 2 elements:")
	popped1 = pop(stack)
	popped2 = pop(stack)
	print("Popped:", popped1, popped2)

	# Display remaining stack
	print("\nRemaining stack after popping 2 elements:")
	display(stack)


if __name__ == "__main__":
	main()

