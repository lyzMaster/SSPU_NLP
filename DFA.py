# 《自然语言处理综论》p23

class FSA:
    def __init__(self, num_states=0):
        self.num_states = num_states   # 状态数
        self.transitions = {}   # 状态转移函数
        self.final_states = set()   # 最终状态

    # s: 字符，currentState:目前状态，newState:目标状态
    def add_transition(self, s, currentState, newState):
        self.transitions[(s, currentState)] = newState

    def set_final_state(self, final):
        self.final_states.add(final)

    def lookup(self, current, s):
        if (s, current) in self.transitions:
            return self.transitions[(s, current)]
        else:
            return None

    def is_final(self, state):
        return state in self.final_states


def DRecognize(input_str, fsa):
    index = 0
    currentState = "0"

    while True:
        if index == len(input_str):
            if fsa.is_final(currentState):
                return True
            else:
                return False
        elif not fsa.lookup(currentState, input_str[index]):
            return False
        else:
            currentState = fsa.lookup(currentState, input_str[index])
            index += 1


# baa(...)!的识别

sheep = FSA(5)

sheep.add_transition("b", "0", "1")
sheep.add_transition("a", "1", "2")
sheep.add_transition("a", "2", "3")
sheep.add_transition("a", "3", "3")
sheep.add_transition("!", "3", "4")

sheep.set_final_state("4")

print(DRecognize("ba!", sheep))
print(DRecognize("bbba!", sheep))
print(DRecognize("baaaaaaa!", sheep))
