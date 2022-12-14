# Copyright 2022 joetjo https://github.com/joetjo/MarkdownHelper
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from abc import ABC, abstractmethod


class EventListener(ABC):
    pass

    @abstractmethod
    def newGame(self, game):
        Log.debug("[ABC Impl] New game detected {} ({})".format(game.getName(), game.process.getPath()))

    @abstractmethod
    def refreshDone(self, current_game, platform_list_updated, others):
        pass

    @abstractmethod
    def endGame(self, proc):
        Log.debug("[ABC Impl] End game detected {} ({})".format(proc.getName(), proc.getPath()))
