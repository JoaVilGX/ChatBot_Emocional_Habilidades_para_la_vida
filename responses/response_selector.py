# SELECTOR DE RESPUESTAS ALEATORIAS - Elige 1 de 3 respuestas posibles
# Contenido: Sistema de variabilidad para evitar respuestas repetitivas

import random
from typing import List, Optional
from responses.formatter import format_response  # Añadir esta importación

class ResponseSelector:
    """
    Selecciona respuestas aleatorias manteniendo coherencia.
    Evita repetir la misma respuesta consecutivamente.
    """

    def __init__(self):
        self.last_responses = {}
        self.max_history = 3

    def select_random_response(self, responses: List[str], user_id: Optional[str] = None) -> str:
        """
        Selecciona una respuesta aleatoria de la lista,
        evitando repetir las últimas respuestas dadas al usuario.

        Args:
            responses: Lista de respuestas posibles (debe tener al menos 3)
            user_id: ID del usuario para mantener historial

        Returns:
            Respuesta seleccionada aleatoriamente, formateada
        """
        if not responses:
            return "Lo siento, no tengo información sobre eso en este momento."

        # Si hay menos de 3 respuestas, completar con variaciones
        if len(responses) < 3:
            responses = self._generate_variations(responses)

        # Para usuarios específicos, evitar repeticiones
        if user_id:
            user_history = self.last_responses.get(user_id, [])

            # Filtrar respuestas que no estén en el historial reciente
            available_responses = [r for r in responses if r not in user_history]

            # Si todas están en el historio, limpiar historial
            if not available_responses:
                available_responses = responses
                user_history = []

            # Seleccionar respuesta aleatoria
            selected = random.choice(available_responses)

            # Actualizar historial
            user_history.append(selected)
            if len(user_history) > self.max_history:
                user_history.pop(0)

            self.last_responses[user_id] = user_history
            return format_response(selected)  # Formatear la respuesta

        # Para usuarios anónimos, selección simple
        return format_response(random.choice(responses))  # Formatear la respuesta

    def _generate_variations(self, base_responses: List[str]) -> List[str]:
        """Genera variaciones de respuestas si hay menos de 3"""
        variations = []

        for response in base_responses:
            # Añadir variaciones con diferentes formatos
            variations.append(response)

            # Variación 1: Formato más directo
            if "Puedes intentar" in response:
                variations.append(response.replace("Puedes intentar", "Te sugiero"))

            # Variación 2: Formato más empático
            if "Es importante" in response:
                variations.append(response.replace("Es importante", "Considera que es valioso"))

        return variations[:3]  # Asegurar máximo 3 respuestas