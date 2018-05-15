#!/usr/bin/env python3


def eval_input_float(prompt):
    user_entry = input(prompt)
    try:
        parsed_float = float(eval(user_entry))
        q_sig = False
    except:
        parsed_float = None
        q_sig = True
    return parsed_float, q_sig


def prompt_user():
    d = {
        'working_years': 'Enter the number of remaining working years: ',
        'ann_contr': 'Enter the estimated yearly contribution, in USD: ',
        'ann_growth': 'Enter the estimated yearly rate of return (i.e. 0.07 for 7% rate of return): ',
        'contr_growth': 'Enter the estimated contribution growth (i.e. 0.04 for a 4% growth): ',
        'account_val': 'Enter the current retirement account value: '
    }

    quit_signal = False

    for var in ['working_years', 'ann_contr', 'ann_growth', 'contr_growth', 'account_val']:
        d[var], quit_signal = eval_input_float(d[var])
        if quit_signal:
            break
    
    return d, quit_signal


def calculate_finances(working_years, account_val, ann_growth, contr_growth, ann_contr):
    for i in range(0, working_years):
        if ann_contr < 18000:
            if i == 0:
                account_val = account_val + ann_contr
                account_val = account_val * (ann_growth + 1)
            else:
                ann_contr = ann_contr * (contr_growth + 1)
                account_val = account_val + ann_contr
                account_val = account_val * (1 + ann_growth)
        else:
            ann_contr = 18000
            account_val = account_val + ann_contr
            account_val = account_val * (ann_growth + 1)
    est_month_income = (account_val * ann_growth) / 12.0
    return round(account_val, 2), round(est_month_income, 2)


if __name__ == '__main__':
    d, quit_signal = prompt_user()
    if quit_signal:
        print('You have selected to quit. Thanks and have a good day!')
    else:
        account_val, est_month_income = calculate_finances(int(d['working_years']), d['account_val'], d['ann_growth'], d['contr_growth'], d['ann_contr'])
        print("The estimated account value is: \t $", account_val, 2)
        print("Your estimated monthly income at retirement would be: \t $", est_month_income , 2)

