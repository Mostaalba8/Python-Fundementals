def splitting_bill(total: int, participants: int) -> float:
    return total/participants

try:
    print(splitting_bill(100,0))
except:
    print('Entered in expect')
    raise  # using raise to bring the original message of the exception 