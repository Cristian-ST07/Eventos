#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para traducir automáticamente el sitio web Evently al español
"""

import os
import re
from pathlib import Path

# Diccionario de traducciones
translations = {
    # Títulos de páginas
    'Index - Evently Bootstrap Template': 'Evently - Eventos Completos',
    'About - Evently Bootstrap Template': 'Nosotros - Evently',
    'Contact - Evently Bootstrap Template': 'Contacto - Evently',
    'Schedule - Evently Bootstrap Template': 'Programa - Evently',
    'Speakers - Evently Bootstrap Template': 'Expositores - Evently',
    'Venue - Evently Bootstrap Template': 'Sede - Evently',
    'Tickets - Evently Bootstrap Template': 'Entradas - Evently',
    'Gallery - Evently Bootstrap Template': 'Galería - Evently',
    'Terms - Evently Bootstrap Template': 'Términos - Evently',
    'Privacy - Evently Bootstrap Template': 'Privacidad - Evently',
    
    # Navegación
    'Home': 'Inicio',
    'About': 'Nosotros',
    'Schedule': 'Programa',
    'Speakers': 'Expositores',
    'Venue': 'Sede',
    'Contact': 'Contacto',
    'Tickets': 'Entradas',
    'Gallery': 'Galería',
    'Terms': 'Términos',
    'Privacy': 'Privacidad',
    'More Pages': 'Más Páginas',
    'Speaker Details': 'Detalles del Expositor',
    'Buy Tickets': 'Comprar Entradas',
    'Dropdown': 'Servicios',
    'Dropdown 1': 'Eventos Corporativos',
    'Dropdown 2': 'Planificación',
    'Dropdown 3': 'Logística',
    'Dropdown 4': 'Marketing',
    'Deep Dropdown': 'Tipos de Eventos',
    'Deep Dropdown 1': 'Conferencias',
    'Deep Dropdown 2': 'Seminarios',
    'Deep Dropdown 3': 'Talleres',
    'Deep Dropdown 4': 'Networking',
    'Deep Dropdown 5': 'Lanzamientos',
    
    # Contenido principal
    'Global Executive Leadership Summit 2026': 'Cumbre Global de Liderazgo Ejecutivo 2026',
    'Connect with industry pioneers, explore cutting-edge strategies, and shape the future of business leadership in an exclusive three-day experience.': 'Conecta con pioneros de la industria, explora estrategias innovadoras y moldea el futuro del liderazgo empresarial en una experiencia exclusiva de tres días.',
    'Event Starts In': 'El Evento Comienza En',
    'Days': 'Días',
    'Hours': 'Horas',
    'Minutes': 'Minutos',
    'Seconds': 'Segundos',
    'Secure Your Seat': 'Reserva tu Lugar',
    'View Speakers': 'Ver Expositores',
    'Limited to 200 executive participants • Early bird pricing ends January 31st': 'Limitado a 200 participantes ejecutivos • Precios especiales terminan el 31 de enero',
    'Proudly supported by industry leaders': 'Orgullosamente apoyado por líderes de la industria',
    
    # Sección intro
    'The Definitive Tech Innovation Summit': 'La Cumbre Definitiva de Innovación Tecnológica',
    'Morbi auctor ipsum vel leo cursus, ac tempor augue tempus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nulla facilisi. Fusce vitae magna non nulla vulputate tincidunt.': 'Evently es líder en la organización de eventos tecnológicos de clase mundial. Nuestro equipo experto garantiza experiencias excepcionales que conectan a profesionales, innovadores y líderes de la industria en un ambiente de colaboración y aprendizaje.',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa.': 'Durante más de una década, hemos sido pioneros en la creación de espacios donde las ideas revolucionarias cobran vida. Nuestros eventos combinan contenido de vanguardia, networking de alto nivel y experiencias inmersivas que transforman la manera en que las empresas abordan la innovación.',
    'View Full Agenda': 'Ver Agenda Completa',
    'Meet the Speakers': 'Conocer Expositores',
    'Global Networking': 'Networking Global',
    'Connect with industry leaders from 60+ countries': 'Conecta con líderes de la industria de más de 60 países',
    'Innovation Showcase': 'Muestra de Innovación',
    'Discover cutting-edge technologies and startups': 'Descubre tecnologías de vanguardia y startups emergentes',
    'Our mission has always been to bridge the gap between visionary ideas and practical implementation. This summit represents the culmination of years of bringing together the brightest minds in technology.': 'Nuestra misión siempre ha sido cerrar la brecha entre las ideas visionarias y la implementación práctica. Esta cumbre representa la culminación de años reuniendo a las mentes más brillantes en tecnología.',
    'Founder & Event Director': 'Fundadora y Directora de Eventos',
    
    # Expositores
    'Featured Speakers': 'Expositores Destacados',
    'Necessitatibus eius consequatur ex aliquid fuga eum quidem sint consectetur velit': 'Conoce a los expertos y líderes de la industria que compartirán sus conocimientos y experiencias',
    'Keynote Speaker': 'Expositora Principal',
    'Panel Speaker': 'Expositor de Panel',
    'Chief Technology Officer': 'Directora de Tecnología',
    'VP of Product Strategy': 'VP de Estrategia de Producto',
    'Session: "The Future of AI in Business"': 'Sesión: "El Futuro de la IA en los Negocios"',
    'Session: "Digital Transformation Strategies"': 'Sesión: "Estrategias de Transformación Digital"',
    'View Profile': 'Ver Perfil',
    'Design Director': 'Directora de Diseño',
    'Data Scientist': 'Científico de Datos',
    'Marketing Expert': 'Experta en Marketing',
    'CEO & Founder': 'CEO y Fundador',
    'Design Thinking Workshop': 'Taller de Design Thinking',
    'Big Data Analytics': 'Análisis de Big Data',
    'Digital Marketing Trends': 'Tendencias de Marketing Digital',
    'Entrepreneurship Panel': 'Panel de Emprendimiento',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.': 'La innovación tecnológica no es solo sobre crear nuevas herramientas, sino sobre transformar la manera en que vivimos y trabajamos. En Evently, creamos espacios donde estas transformaciones cobran vida.',
    
    # Programa
    'Schedule': 'Programa',
    'Descubre la agenda completa de tres días llena de contenido innovador y networking de alto nivel': 'Descubre la agenda completa de tres días llena de contenido innovador y networking de alto nivel',
    'Day 1 - March 15': 'Día 1 - 15 de Marzo',
    'Day 2 - March 16': 'Día 2 - 16 de Marzo',
    'Day 3 - March 17': 'Día 3 - 17 de Marzo',
    'Development Track': 'Pista de Desarrollo',
    'Design Track': 'Pista de Diseño',
    'Business Track': 'Pista de Negocios',
    'Keynote': 'Conferencia Principal',
    'Future of Digital Innovation': 'El Futuro de la Innovación Digital',
    'Main Hall': 'Salón Principal',
    'Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.': 'Explora las tendencias emergentes que están transformando la industria tecnológica y descubre cómo las empresas pueden adaptarse al futuro digital.',
    
    # Entradas
    'General Admission': 'Entrada General',
    '/ticket': '/entrada',
    '3-Day Access': 'Acceso de 3 Días',
    'Access to all conference sessions': 'Acceso a todas las sesiones de la conferencia',
    'Welcome reception networking': 'Networking en la recepción de bienvenida',
    'Coffee breaks and lunch included': 'Pausas para café y almuerzo incluidos',
    'Digital conference materials': 'Materiales digitales de la conferencia',
    'Certificate of attendance': 'Certificado de asistencia',
    'Register Now': 'Registrarse Ahora',
    '250 tickets remaining': '250 entradas restantes',
    'Most Popular': 'Más Popular',
    'VIP Experience': 'Experiencia VIP',
    '3-Day Premium Access': 'Acceso Premium de 3 Días',
    'All General Admission benefits': 'Todos los beneficios de Entrada General',
    'Reserved front row seating': 'Asientos reservados en primera fila',
    'Exclusive VIP networking lounge': 'Sala de networking VIP exclusiva',
    'Meet & greet with keynote speakers': 'Encuentro con expositores principales',
    'Premium swag bag worth $150': 'Bolsa de regalos premium valorada en $150',
    'Private dinner with industry leaders': 'Cena privada con líderes de la industria',
    'Get VIP Access': 'Obtener Acceso VIP',
    'Limited to 50 attendees': 'Limitado a 50 asistentes',
    'Student Pass': 'Pase Estudiantil',
    '3-Day Student Access': 'Acceso Estudiantil de 3 Días',
    'Student networking events': 'Eventos de networking para estudiantes',
    'Career fair participation': 'Participación en feria de carreras',
    'Mentorship program eligibility': 'Elegibilidad para programa de mentoría',
    'Student resource kit': 'Kit de recursos para estudiantes',
    'Student Registration': 'Registro Estudiantil',
    'Valid student ID required': 'Se requiere identificación estudiantil válida',
    
    # Call to Action
    'Ready to Transform Your Professional Network?': '¿Listo para Transformar tu Red Profesional?',
    'Join industry leaders and innovators at the premier professional development conference. Secure your place among 5,000+ forward-thinking professionals from 25+ countries.': 'Únete a líderes de la industria e innovadores en la conferencia de desarrollo profesional más importante. Asegura tu lugar entre más de 5,000 profesionales visionarios de más de 25 países.',
    'Expected Attendees': 'Asistentes Esperados',
    'Expert Speakers': 'Expositores Expertos',
    'Countries Represented': 'Países Representados',
    'Days of Excellence': 'Días de Excelencia',
    'Early Bird Registration Ends Soon': 'El Registro Anticipado Termina Pronto',
    'Secure your spot at the exclusive rate. Limited availability for premium networking sessions and workshop access.': 'Asegura tu lugar a la tarifa exclusiva. Disponibilidad limitada para sesiones de networking premium y acceso a talleres.',
    'Download Brochure': 'Descargar Folleto',
    'Secure payment processing • Full refund policy • ISO certified event management': 'Procesamiento de pago seguro • Política de reembolso completo • Gestión de eventos certificada ISO',
    
    # Testimonios
    'Testimonials': 'Testimonios',
    'Lo que dicen nuestros participantes sobre sus experiencias en eventos Evently': 'Lo que dicen nuestros participantes sobre sus experiencias en eventos Evently',
    
    # Footer
    'Useful Links': 'Enlaces Útiles',
    'Our Services': 'Nuestros Servicios',
    'Web Design': 'Diseño Web',
    'Web Development': 'Desarrollo Web',
    'Product Management': 'Gestión de Productos',
    'Graphic Design': 'Diseño Gráfico',
    'Hic solutasetp': 'Eventos Especializados',
    'Molestiae accusamus iure': 'Conferencias Tecnológicas',
    'Excepturi dignissimos': 'Seminarios Empresariales',
    'Suscipit distinctio': 'Talleres de Innovación',
    'Dilecta': 'Eventos de Networking',
    'Sit quas consectetur': 'Lanzamientos de Productos',
    'Nobis illum': 'Recursos',
    'Ipsam': 'Blog de Eventos',
    'Laudantium dolorum': 'Guías de Planificación',
    'Dinera': 'Casos de Éxito',
    'Trodelas': 'Herramientas',
    'Flexo': 'Soporte',
    'Copyright': 'Copyright',
    'MyWebsite': 'Evently',
    'All Rights Reserved': 'Todos los Derechos Reservados',
    'Designed by': 'Diseñado por',
    
    # Páginas específicas
    'Esse dolorum voluptatum ullam est sint nemo et est ipsa porro placeat quibusdam quia assumenda numquam molestias.': 'Descubre la historia detrás de Evently y cómo hemos transformado la industria de eventos durante más de una década.',
    'Estamos aquí para ayudarte a crear el evento perfecto. Contáctanos y descubre cómo podemos hacer realidad tu visión.': 'Estamos aquí para ayudarte a crear el evento perfecto. Contáctanos y descubre cómo podemos hacer realidad tu visión.',
}

def translate_file(file_path):
    """Traducir un archivo HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Aplicar traducciones
        for english, spanish in translations.items():
            content = content.replace(english, spanish)
        
        # Traducciones específicas para el footer
        footer_text = "Este es un demo de Web Impulsa. ¿Quieres un sitio como este para tu negocio? Escríbenos al WhatsApp +593 98 374 9609."
        
        # Reemplazar información de contacto en el footer
        contact_pattern = r'<div class="footer-contact pt-3">\s*<p>A108 Adam Street</p>\s*<p>New York, NY 535022</p>\s*<p class="mt-3"><strong>Phone:</strong> <span>\+1 5589 55488 55</span></p>\s*<p><strong>Email:</strong> <span>info@example\.com</span></p>\s*</div>'
        contact_replacement = f'<div class="footer-contact pt-3">\n            <p>{footer_text}</p>\n          </div>'
        content = re.sub(contact_pattern, contact_replacement, content, flags=re.MULTILINE | re.DOTALL)
        
        # Reemplazar copyright
        copyright_pattern = r'<div class="credits">\s*<!-- All the links in the footer should remain intact\. -->\s*<!-- You can delete the links only if you\'ve purchased the pro version\. -->\s*<!-- Licensing information: https://bootstrapmade\.com/license/ -->\s*<!-- Purchase the pro version with working PHP/AJAX contact form: \[buy-url\] -->\s*Designed by <a href="https://bootstrapmade\.com/">BootstrapMade</a>\s*</div>'
        copyright_replacement = f'<div class="credits">\n        <p>{footer_text}</p>\n      </div>'
        content = re.sub(copyright_pattern, copyright_replacement, content, flags=re.MULTILINE | re.DOTALL)
        
        # Guardar archivo traducido
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Traducido: {file_path}")
        return True
        
    except Exception as e:
        print(f"✗ Error traduciendo {file_path}: {e}")
        return False

def main():
    """Función principal"""
    html_files = [
        'index.html',
        'about.html', 
        'contact.html',
        'schedule.html',
        'speakers.html',
        'venue.html',
        'tickets.html',
        'buy-tickets.html',
        'gallery.html',
        'speaker-details.html',
        'terms.html',
        'privacy.html',
        '404.html',
        'sponsors.html',
        'starter-page.html'
    ]
    
    print("🚀 Iniciando traducción del sitio web Evently...")
    
    success_count = 0
    for file_name in html_files:
        if os.path.exists(file_name):
            if translate_file(file_name):
                success_count += 1
        else:
            print(f"⚠️  Archivo no encontrado: {file_name}")
    
    print(f"\n✅ Traducción completada: {success_count}/{len(html_files)} archivos procesados")
    print("🎉 El sitio web Evently ha sido traducido al español exitosamente!")

if __name__ == "__main__":
    main()
