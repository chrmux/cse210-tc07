from game import constants
from game.words import Words
import random

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.
        Args:
            self (Director): An instance of Director.
        """
        self.words = self.get_words()
        self.displayed_words = []
        self.displayed_words.append(self.words[random.randint(0, len(self.words) - 1)])



    def get_words(self):
        f = open("speed/game/words.txt") # if I use this (constants.LIBRARY) this is the error --> TypeError: expected str, bytes or os.PathLike object, not _io.TextIOWrapper
        word_list = f.read().split('\n')
        random.shuffle(word_list)
        return [Words(self, i) for i in word_list if i != '']

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.
        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.flush_buffer()
