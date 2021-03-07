import usb


usbs = usb.core.find(find_all=True)
print(f'Standart list: {sum(1 for i in usbs)}')
