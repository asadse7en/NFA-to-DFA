def nfa_to_dfa(nfa_states, nfa_transitions, nfa_start_state, nfa_accept_states):
    dfa_states = []
    dfa_transitions = {}
    stack = [frozenset(epsilon_closure([nfa_start_state], nfa_transitions))]

    while stack:
        current_states = stack.pop()
        dfa_states.append(current_states)

        for symbol in nfa_transitions[nfa_states[0]]:
            next_states = set()
            for state in current_states:
                if symbol in nfa_transitions[state]:
                    next_states.update(epsilon_closure([nfa_transitions[state][symbol]], nfa_transitions))

            next_states = frozenset(next_states)

            dfa_transitions.setdefault(current_states, {})[symbol] = next_states

            if next_states not in dfa_states and next_states:
                stack.append(next_states)

    dfa_accept_states = [state for state in dfa_states if any(state in nfa_accept_states for nfa_accept_states in nfa_accept_states)]

    return dfa_states, dfa_transitions, dfa_accept_states

def main():
    nfa_states = input("Enter NFA states (comma-separated): ").split(',')
    nfa_transitions = get_transitions(nfa_states)
    nfa_start_state = input("Enter the start state: ")
    nfa_accept_states = input("Enter NFA accept states (comma-separated): ").split(',')

    dfa_states, dfa_transitions, dfa_accept_states = nfa_to_dfa(nfa_states, nfa_transitions, nfa_start_state, nfa_accept_states)

    print("\nDFA States:")
    for i, state in enumerate(dfa_states):
        print(f"State {i}: {state}")

    print("\nDFA Transitions:")
    for state, transitions in dfa_transitions.items():
        for symbol, next_state in transitions.items():
            print(f"{state} --({symbol})--> {next_state}")

    print("\nDFA Accept States:")
    for i, state in enumerate(dfa_accept_states):
        print(f"State {i}: {state}")

if __name__ == "__main__":
    main()
