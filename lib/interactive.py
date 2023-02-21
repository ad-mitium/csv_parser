#!/usr/bin/env python3

def exit_on_error(unit_test=False):
    answer = input("Continue with default options? [y/N]  ").lower()
    if answer == 'y':
        print("Continuing with default options")
    else:
        print("Exiting.")
        raise SystemExit(0)

def continue_check(item, unit_test=False):
    limit=10        # 10 tries or quit
    answer=''
    for i in (range(limit, -1, -1)):
        if i > 0:
            try: 
                answer = input("Do you wish to get data for "+item+"? (y/N) ").lower()
                if answer== 'y' :
                    print("Data for "+item+" will be collected")
                    return True
                elif answer == '' or answer == 'n':
                    print(item+" will not be collected")
                    return False
                else:
                    raise(ValueError())
            except ValueError:
                answer = input("Do you wish to get data for "+item+"? (y/N) ").lower()
                i=i-1
        else:
            raise SystemExit('Too many failures to enter a valid integer, exiting.')

##### For Unit testing #####
if (__name__ == '__main__'):    #

    unit_test = True     # 

    state=continue_check("Item")
    print (state)
    exit_on_error(unit_test)
else:
    print('', end='')